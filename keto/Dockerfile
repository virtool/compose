FROM oryd/keto:v0.10.0-alpha.0
COPY keto.yaml /keto.yaml
COPY namespaces /namespaces
RUN ls /
ENTRYPOINT ["keto"]
CMD ["serve", "--config", "/keto.yaml"]
# CMD ["migrate", "up", "--yes", "--config", "/keto.yaml"]