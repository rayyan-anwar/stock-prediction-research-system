# Stock Prediction Research System

Research-oriented time-series forecasting platform for stock-price analysis, feature engineering, leakage-aware evaluation, baseline ML forecasting, and experiment documentation.

**Author:** Rayyan Anwar  
**Positioning:** AI/ML Research · Engineering · Technology Management

## Architecture
Market Data → Validation → Feature Engineering → Temporal Split → ML Baseline → Evaluation → Forecast API / Research Dashboard

## Features
- OHLCV-style CSV analysis
- Lag, return, moving-average and volume features
- Chronological train/test methodology
- Random Forest regression baseline
- Direction estimate
- FastAPI REST service
- Streamlit research dashboard
- Pytest
- Docker + docker-compose
- GitHub Actions CI
- Research protocol and model card

## Research Roadmap
Walk-forward validation, XGBoost/deep temporal models, uncertainty intervals, regime analysis, transaction-cost-aware backtesting, and SHAP/permutation-based explainability.

## Responsible Use
Research and education only. Forecasts are not financial advice and must not be treated as guaranteed investment predictions.

## Run
```bash
pip install -r requirements.txt
uvicorn backend.app.main:app --reload
streamlit run dashboard/app.py
pytest -q
```
