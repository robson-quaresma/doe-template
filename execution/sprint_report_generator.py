#!/usr/bin/env python3
"""
Sprint Report Generator - Script Principal

Gera relatório automatizado de sprint coletando dados de Jira, GitHub e CI/CD.
Parte do DOE Framework - Camada de EXECUTION (determinística).

Usage:
    python3 execution/sprint_report_generator.py --sprint-id "SPRINT-42" --team "platform"
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()


class SprintReportGenerator:
    """
    Gerador de relatório de sprint.
    Orquestra coleta de dados, processamento e geração de output.
    """
    
    def __init__(self, sprint_id: str, team: Optional[str] = None, 
                 include_graphs: bool = True, notify_slack: bool = True):
        """
        Inicializa o gerador de relatório.
        
        Args:
            sprint_id: ID da sprint no Jira (ex: "SPRINT-42")
            team: Nome da equipe (None = todas as equipes)
            include_graphs: Se deve gerar gráficos visuais
            notify_slack: Se deve enviar notificação no Slack
        """
        self.sprint_id = sprint_id
        self.team = team
        self.include_graphs = include_graphs
        self.notify_slack = notify_slack
        
        # Diretórios de trabalho
        self.tmp_dir = ".tmp"
        self.charts_dir = f"{self.tmp_dir}/charts"
        self.logs_dir = f"{self.tmp_dir}/logs"
        
        # Garante que diretórios existem
        self._ensure_directories()
        
        # Setup de logging
        self.log_file = f"{self.logs_dir}/sprint_report_{sprint_id}.log"
        self._setup_logging()
    
    def _ensure_directories(self):
        """Cria diretórios necessários se não existirem."""
        for directory in [self.tmp_dir, self.charts_dir, self.logs_dir]:
            os.makedirs(directory, exist_ok=True)
    
    def _setup_logging(self):
        """Configura sistema de logging."""
        self.log(f"=== Sprint Report Generation Started ===")
        self.log(f"Sprint ID: {self.sprint_id}")
        self.log(f"Team: {self.team or 'ALL'}")
        self.log(f"Timestamp: {datetime.now().isoformat()}")
    
    def log(self, message: str, level: str = "INFO"):
        """
        Registra mensagem no log.
        
        Args:
            message: Mensagem a ser registrada
            level: Nível do log (INFO, WARNING, ERROR)
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        print(log_entry)
        
        with open(self.log_file, 'a') as f:
            f.write(log_entry + '\n')
    
    def validate_inputs(self) -> bool:
        """
        Valida inputs antes de processar.
        
        Returns:
            True se inputs válidos, False caso contrário
        """
        self.log("Validating inputs...")
        
        # Validar formato do sprint_id
        if not self.sprint_id or len(self.sprint_id) < 3:
            self.log("Invalid sprint_id format", level="ERROR")
            return False
        
        # Validar variáveis de ambiente necessárias
        required_env_vars = [
            "JIRA_URL",
            "JIRA_API_TOKEN",
            "GITHUB_TOKEN"
        ]
        
        missing_vars = []
        for var in required_env_vars:
            if not os.getenv(var):
                missing_vars.append(var)
        
        if missing_vars:
            self.log(f"Missing environment variables: {', '.join(missing_vars)}", 
                    level="ERROR")
            return False
        
        self.log("✓ Inputs validated successfully")
        return True
    
    def collect_jira_data(self) -> Optional[Dict]:
        """
        Coleta dados do Jira.
        
        Returns:
            Dicionário com dados do Jira ou None em caso de erro
        """
        self.log("Collecting Jira data...")
        
        cache_file = f"{self.tmp_dir}/jira_data_{self.sprint_id}.json"
        
        try:
            # Simula coleta de dados do Jira
            # Em produção, aqui estaria a chamada real à API Jira
            jira_data = {
                "sprint_id": self.sprint_id,
                "team": self.team,
                "period": {
                    "start": "2024-01-20",
                    "end": "2024-02-02"
                },
                "points": {
                    "planned": 42,
                    "completed": 38,
                    "completion_rate": 0.90
                },
                "issues": [
                    {
                        "key": "PLAT-123",
                        "summary": "Migrate service X to GCP",
                        "status": "Done",
                        "points": 8
                    },
                    {
                        "key": "PLAT-124",
                        "summary": "Implement monitoring",
                        "status": "Done",
                        "points": 5
                    }
                ]
            }
            
            # Salva em cache
            with open(cache_file, 'w') as f:
                json.dump(jira_data, f, indent=2)
            
            self.log(f"✓ Jira data collected: {len(jira_data['issues'])} issues")
            return jira_data
            
        except Exception as e:
            self.log(f"Error collecting Jira data: {str(e)}", level="ERROR")
            
            # Tenta usar cache se disponível
            if os.path.exists(cache_file):
                self.log("Using cached Jira data (may be stale)", level="WARNING")
                with open(cache_file, 'r') as f:
                    return json.load(f)
            
            return None
    
    def collect_github_data(self) -> Optional[Dict]:
        """
        Coleta dados do GitHub.
        
        Returns:
            Dicionário com dados do GitHub ou None em caso de erro
        """
        self.log("Collecting GitHub data...")
        
        team_suffix = f"_{self.team}" if self.team else "_all"
        cache_file = f"{self.tmp_dir}/github_data{team_suffix}.json"
        
        try:
            # Simula coleta de dados do GitHub
            # Em produção, aqui estaria a chamada real à API GitHub
            github_data = {
                "team": self.team,
                "period_days": 14,
                "prs": {
                    "total_merged": 45,
                    "avg_review_time_hours": 6.2,
                    "pending": 8
                },
                "top_reviewers": [
                    {"name": "joao", "count": 12},
                    {"name": "maria", "count": 10},
                    {"name": "pedro", "count": 9}
                ]
            }
            
            # Salva em cache
            with open(cache_file, 'w') as f:
                json.dump(github_data, f, indent=2)
            
            self.log(f"✓ GitHub data collected: {github_data['prs']['total_merged']} PRs")
            return github_data
            
        except Exception as e:
            self.log(f"Error collecting GitHub data: {str(e)}", level="ERROR")
            
            # Tenta usar cache
            if os.path.exists(cache_file):
                self.log("Using cached GitHub data (may be stale)", level="WARNING")
                with open(cache_file, 'r') as f:
                    return json.load(f)
            
            return None
    
    def collect_cicd_data(self) -> Optional[Dict]:
        """
        Coleta dados de CI/CD (Jenkins/CircleCI/etc).
        
        Returns:
            Dicionário com dados de deployment ou None em caso de erro
        """
        self.log("Collecting CI/CD data...")
        
        team_suffix = f"_{self.team}" if self.team else "_all"
        cache_file = f"{self.tmp_dir}/cicd_data{team_suffix}.json"
        
        try:
            # Simula coleta de dados de CI/CD
            cicd_data = {
                "team": self.team,
                "period_days": 14,
                "deployments": {
                    "total": 18,
                    "successful": 17,
                    "failed": 1,
                    "success_rate": 0.94
                },
                "frequency_per_day": 1.3
            }
            
            # Salva em cache
            with open(cache_file, 'w') as f:
                json.dump(cicd_data, f, indent=2)
            
            self.log(f"✓ CI/CD data collected: {cicd_data['deployments']['total']} deployments")
            return cicd_data
            
        except Exception as e:
            self.log(f"Error collecting CI/CD data: {str(e)}", level="ERROR")
            
            if os.path.exists(cache_file):
                self.log("Using cached CI/CD data (may be stale)", level="WARNING")
                with open(cache_file, 'r') as f:
                    return json.load(f)
            
            return None
    
    def aggregate_data(self, jira_data: Dict, github_data: Dict, 
                      cicd_data: Dict) -> Dict:
        """
        Agrega dados de todas as fontes.
        
        Args:
            jira_data: Dados do Jira
            github_data: Dados do GitHub
            cicd_data: Dados de CI/CD
            
        Returns:
            Dicionário com dados agregados
        """
        self.log("Aggregating data from all sources...")
        
        aggregated = {
            "sprint": jira_data,
            "code_review": github_data,
            "deployment": cicd_data,
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "sprint_id": self.sprint_id,
                "team": self.team
            }
        }
        
        # Salva dados agregados
        output_file = f"{self.tmp_dir}/aggregated_data_{self.sprint_id}.json"
        with open(output_file, 'w') as f:
            json.dump(aggregated, f, indent=2)
        
        self.log(f"✓ Data aggregated and saved to {output_file}")
        return aggregated
    
    def generate_report(self, data: Dict) -> str:
        """
        Gera relatório formatado.
        
        Args:
            data: Dados agregados
            
        Returns:
            URL do Google Doc gerado
        """
        self.log("Generating report document...")
        
        # Em produção, aqui estaria a geração real do Google Doc
        # Por agora, simula criação de documento
        
        report_content = f"""
SPRINT {self.sprint_id} - REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Team: {self.team or 'ALL TEAMS'}

═══════════════════════════════════════

1. SPRINT OVERVIEW
   Points Planned: {data['sprint']['points']['planned']}
   Points Completed: {data['sprint']['points']['completed']}
   Completion Rate: {data['sprint']['points']['completion_rate'] * 100:.1f}%

2. CODE REVIEW METRICS
   PRs Merged: {data['code_review']['prs']['total_merged']}
   Avg Review Time: {data['code_review']['prs']['avg_review_time_hours']:.1f}h
   Pending PRs: {data['code_review']['prs']['pending']}

3. DEPLOYMENT METRICS
   Total Deploys: {data['deployment']['deployments']['total']}
   Success Rate: {data['deployment']['deployments']['success_rate'] * 100:.1f}%
   Deploy Frequency: {data['deployment']['frequency_per_day']:.1f}/day

═══════════════════════════════════════
"""
        
        # Salva como texto temporário
        temp_report = f"{self.tmp_dir}/report_{self.sprint_id}.txt"
        with open(temp_report, 'w') as f:
            f.write(report_content)
        
        # URL simulado do Google Doc
        doc_url = f"https://docs.google.com/document/d/SIMULATED_{self.sprint_id}"
        
        self.log(f"✓ Report generated: {doc_url}")
        return doc_url
    
    def send_notification(self, doc_url: str) -> bool:
        """
        Envia notificação no Slack.
        
        Args:
            doc_url: URL do documento gerado
            
        Returns:
            True se notificação enviada com sucesso
        """
        if not self.notify_slack:
            self.log("Slack notification disabled, skipping...")
            return True
        
        self.log("Sending Slack notification...")
        
        try:
            # Em produção, aqui estaria a chamada ao Slack Webhook
            # Por agora, simula envio
            
            message = {
                "text": f"✅ Sprint Report gerado para {self.sprint_id}",
                "attachments": [{
                    "color": "good",
                    "fields": [
                        {
                            "title": "Sprint",
                            "value": self.sprint_id,
                            "short": True
                        },
                        {
                            "title": "Team",
                            "value": self.team or "ALL",
                            "short": True
                        },
                        {
                            "title": "Document",
                            "value": f"<{doc_url}|View Report>",
                            "short": False
                        }
                    ]
                }]
            }
            
            self.log(f"✓ Slack notification sent")
            return True
            
        except Exception as e:
            self.log(f"Error sending Slack notification: {str(e)}", level="ERROR")
            return False
    
    def run(self) -> bool:
        """
        Executa todo o processo de geração de relatório.
        
        Returns:
            True se processo completou com sucesso
        """
        try:
            # 1. Validar inputs
            if not self.validate_inputs():
                return False
            
            # 2. Coletar dados (paralelo em produção)
            jira_data = self.collect_jira_data()
            github_data = self.collect_github_data()
            cicd_data = self.collect_cicd_data()
            
            # Verificar se todas as coletas foram bem-sucedidas
            if not all([jira_data, github_data, cicd_data]):
                self.log("Failed to collect all required data", level="ERROR")
                return False
            
            # 3. Agregar dados
            aggregated_data = self.aggregate_data(jira_data, github_data, cicd_data)
            
            # 4. Gerar relatório
            doc_url = self.generate_report(aggregated_data)
            
            # 5. Enviar notificação
            self.send_notification(doc_url)
            
            # Sucesso!
            self.log("=== Sprint Report Generation Completed Successfully ===")
            self.log(f"Report URL: {doc_url}")
            
            return True
            
        except Exception as e:
            self.log(f"Unexpected error: {str(e)}", level="ERROR")
            import traceback
            self.log(traceback.format_exc(), level="ERROR")
            return False


def main():
    """Função principal com argumentos de linha de comando."""
    parser = argparse.ArgumentParser(
        description="Generate automated sprint report"
    )
    
    parser.add_argument(
        "--sprint-id",
        required=True,
        help="Sprint ID from Jira (e.g., SPRINT-42)"
    )
    
    parser.add_argument(
        "--team",
        default=None,
        help="Team name filter (default: all teams)"
    )
    
    parser.add_argument(
        "--include-graphs",
        type=bool,
        default=True,
        help="Include visual charts in report (default: true)"
    )
    
    parser.add_argument(
        "--notify-slack",
        type=bool,
        default=True,
        help="Send Slack notification (default: true)"
    )
    
    args = parser.parse_args()
    
    # Criar e executar gerador
    generator = SprintReportGenerator(
        sprint_id=args.sprint_id,
        team=args.team,
        include_graphs=args.include_graphs,
        notify_slack=args.notify_slack
    )
    
    success = generator.run()
    
    # Return code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
