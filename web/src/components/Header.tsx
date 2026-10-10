function Header() {
  return (
    <header className="border-bottom bg-white">
      <div className="container py-4">
        <div className="fade-in">
          <div className="row align-items-center">
            <div className="col-md-6">
              <div className="d-flex align-items-center gap-2 mb-2">
                <i className="bi bi-shield-check text-success"></i>
                <span className="small fw-semibold text-success">
                  Casino Bonus
                </span>
              </div>
            </div>

            <div className="col-md-6 text-md-end">
              <h1 className="h2 fw-bold mb-2">
                casino welcome bonuses
              </h1>

              <p className="text-secondary mb-0">
                compare bonus amounts, wagering requirements, and minimum deposits
              </p>
            </div>
          </div>
        </div>
      </div>
    </header>
  )
}

export default Header
