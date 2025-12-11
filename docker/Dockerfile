FROM python:3.11-slim
WORKDIR /home/appuser
USER appuser
COPY --chown=appuser:appuser ../api .
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]