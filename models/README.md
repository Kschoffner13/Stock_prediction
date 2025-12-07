# Stock Price Prediction using LSTM and GRU

## Overview
This project provides two recurrent models—**LSTM** and **GRU**—to predict next-day closing prices using the same 5 technical indicators. Both models share identical inputs, training setup, and evaluation metrics.

## Features
The model uses the following 5 features for prediction:

1. **Close** - Historical closing prices
2. **Volume** - Daily trading volume
3. **MA20** - 20-day moving average (captures price trends)
4. **Volatility** - 20-day standard deviation of returns (measures risk)
5. **RSI** - Relative Strength Index (momentum indicator, 14-day)

## Model Architectures
- **LSTM**: Bidirectional, 2 layers, 64 hidden units, 20% dropout
- **GRU**: Bidirectional, 2 layers, 64 hidden units, 20% dropout
- **Input**: 60 days of historical data (5 features per day)
- **Output**: Next day's closing price

## How to Run

1. Open a notebook: `lstm/LSTM.ipynb` or `GRU/GRU.ipynb`.
2. Set your target stock (search for `target_ticker` near the top):
   ```python
   target_ticker = "AAPL"  # Any symbol present in the dataset
   ```
3. Run all cells sequentially from top to bottom.

## Training Details
- **Train/Test Split**: 80% training, 20% testing (chronological split)
- **Epochs**: 50
- **Batch Size**: 32
- **Optimizer**: Adam with learning rate scheduler
- **Loss Function**: Mean Squared Error (MSE)

## Evaluation Metrics
The model is evaluated using:
- **RMSE** (Root Mean Squared Error)
- **MAE** (Mean Absolute Error)
- **MAPE** (Mean Absolute Percentage Error)

## Output
After training, the notebook generates:
- Loss curves (training vs. test)
- Actual vs. predicted price comparison plot
- Performance metrics in original price scale

## Data Requirements
- CSV files must be in `data/archive/stocks/` or `data/archive/etfs/`
- Required columns: Date, Open, High, Low, Close, Volume
