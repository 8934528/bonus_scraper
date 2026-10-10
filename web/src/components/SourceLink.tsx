type SourceLinkProps = {
  url: string
}

function SourceLink({ url }: SourceLinkProps) {
  return (
    <a
      href={url}
      target="_blank"
      rel="noreferrer"
      className="text-decoration-none fw-semibold"
      aria-label="View source"
    >
      <i className="bi bi-box-arrow-up-right me-1"></i>
      View
    </a>
  )
}

export default SourceLink
