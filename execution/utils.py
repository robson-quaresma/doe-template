#!/usr/bin/env python3
"""
DOE Framework - Generic Utilities

Common helper functions used across execution scripts.
Part of the EXECUTION layer.
"""

import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional
from dotenv import load_dotenv


class DOEExecutor:
    """
    Base class for DOE execution scripts.
    Provides common functionality: logging, error handling, file management.
    """
    
    def __init__(self, name: str, tmp_dir: str = ".tmp"):
        """
        Initialize executor.
        
        Args:
            name: Name of the executor (used for logging)
            tmp_dir: Temporary directory path
        """
        self.name = name
        self.tmp_dir = tmp_dir
        self.start_time = datetime.now()
        
        # Load environment variables
        load_dotenv()
        
        # Setup directories
        self._setup_directories()
        
        # Setup logging
        self._setup_logging()
    
    def _setup_directories(self):
        """Create necessary directories if they don't exist."""
        directories = [
            self.tmp_dir,
            f"{self.tmp_dir}/logs",
            f"{self.tmp_dir}/data",
            f"{self.tmp_dir}/charts"
        ]
        
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
    
    def _setup_logging(self):
        """Setup logging configuration."""
        log_file = f"{self.tmp_dir}/logs/{self.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] [%(levelname)s] %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        
        self.logger = logging.getLogger(self.name)
        self.logger.info(f"=== {self.name} Started ===")
    
    def log_info(self, message: str):
        """Log info message."""
        self.logger.info(message)
    
    def log_warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)
    
    def log_error(self, message: str):
        """Log error message."""
        self.logger.error(message)
    
    def get_env(self, key: str, required: bool = True) -> Optional[str]:
        """
        Get environment variable.
        
        Args:
            key: Environment variable name
            required: If True, raises error if not found
            
        Returns:
            Environment variable value or None
        """
        value = os.getenv(key)
        
        if required and not value:
            self.log_error(f"Required environment variable not found: {key}")
            raise ValueError(f"Missing required env var: {key}")
        
        return value
    
    def save_json(self, data: Dict[str, Any], filename: str) -> str:
        """
        Save data as JSON file.
        
        Args:
            data: Data to save
            filename: Filename (will be saved in tmp_dir)
            
        Returns:
            Full path to saved file
        """
        filepath = f"{self.tmp_dir}/{filename}"
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        self.log_info(f"Data saved to {filepath}")
        return filepath
    
    def load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        Load JSON file.
        
        Args:
            filename: Filename to load
            
        Returns:
            Loaded data or None if file doesn't exist
        """
        filepath = f"{self.tmp_dir}/{filename}"
        
        if not os.path.exists(filepath):
            self.log_warning(f"File not found: {filepath}")
            return None
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self.log_info(f"Data loaded from {filepath}")
        return data
    
    def get_cache(self, cache_key: str) -> Optional[Dict[str, Any]]:
        """
        Get cached data.
        
        Args:
            cache_key: Cache identifier
            
        Returns:
            Cached data or None
        """
        cache_file = f"cache_{cache_key}.json"
        return self.load_json(cache_file)
    
    def set_cache(self, cache_key: str, data: Dict[str, Any]) -> str:
        """
        Save data to cache.
        
        Args:
            cache_key: Cache identifier
            data: Data to cache
            
        Returns:
            Path to cache file
        """
        cache_file = f"cache_{cache_key}.json"
        return self.save_json(data, cache_file)
    
    def execute_with_retry(self, func, max_retries: int = 3, 
                          backoff_factor: float = 2.0):
        """
        Execute function with retry logic.
        
        Args:
            func: Function to execute
            max_retries: Maximum retry attempts
            backoff_factor: Backoff multiplier
            
        Returns:
            Function result
        """
        import time
        
        for attempt in range(max_retries):
            try:
                return func()
            except Exception as e:
                if attempt == max_retries - 1:
                    self.log_error(f"Failed after {max_retries} attempts: {str(e)}")
                    raise
                
                wait_time = backoff_factor ** attempt
                self.log_warning(f"Attempt {attempt + 1} failed, retrying in {wait_time}s...")
                time.sleep(wait_time)
    
    def finalize(self):
        """Finalize execution and log summary."""
        duration = (datetime.now() - self.start_time).total_seconds()
        self.log_info(f"=== {self.name} Completed in {duration:.2f}s ===")


def validate_required_env_vars(*var_names: str) -> bool:
    """
    Validate that required environment variables are set.
    
    Args:
        var_names: Variable names to check
        
    Returns:
        True if all present, False otherwise
    """
    missing = []
    
    for var in var_names:
        if not os.getenv(var):
            missing.append(var)
    
    if missing:
        print(f"ERROR: Missing required environment variables: {', '.join(missing)}")
        return False
    
    return True


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """
    Format datetime as ISO timestamp.
    
    Args:
        dt: Datetime object (default: now)
        
    Returns:
        ISO formatted timestamp
    """
    if dt is None:
        dt = datetime.now()
    
    return dt.isoformat()


def safe_get(data: Dict, *keys, default=None):
    """
    Safely get nested dictionary value.
    
    Example:
        safe_get(data, 'user', 'profile', 'name', default='Unknown')
    
    Args:
        data: Dictionary to query
        keys: Nested keys
        default: Default value if not found
        
    Returns:
        Value or default
    """
    try:
        result = data
        for key in keys:
            result = result[key]
        return result
    except (KeyError, TypeError):
        return default


if __name__ == "__main__":
    # Example usage
    executor = DOEExecutor("example_executor")
    
    executor.log_info("Starting example execution...")
    
    # Save some data
    test_data = {
        "timestamp": format_timestamp(),
        "status": "success",
        "value": 42
    }
    executor.save_json(test_data, "test_data.json")
    
    # Load it back
    loaded = executor.load_json("test_data.json")
    executor.log_info(f"Loaded data: {loaded}")
    
    executor.finalize()
