FROM alpine
LABEL version="1.0.0"
LABEL repository="http://github.com/khornberg/shell"
LABEL homepage="http://github.com/khornberg/shell"
LABEL com.github.actions.name="GitHub Action for shell"
LABEL com.github.actions.description="Wraps shell for arbitrary execution."
LABEL com.github.actions.icon="package"
LABEL com.github.actions.color="yellow"
COPY "entrypoint.sh" "/entrypoint.sh"
ENTRYPOINT ["/entrypoint.sh"]
CMD ["whoami"]
