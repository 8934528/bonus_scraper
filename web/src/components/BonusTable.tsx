import bonuses from '../data/bonuses.json'
import SourceLink from './SourceLink'

function BonusTable() {
  return (
    <section className="fade-in">
      <div className="mb-4">
        <h2 className="h4 fw-bold mb-1">
          <i className="bi bi-gift me-2 text-success"></i>
          Current bonus offers
        </h2>
      </div>

      <div className="table-responsive bonus-table-wrapper">
        <table className="table align-middle mb-0">
          <thead>
            <tr>
              <th><i className="bi bi-building me-2"></i>Casino</th>
              <th><i className="bi bi-gift me-2"></i>Welcome Bonus</th>
              <th><i className="bi bi-arrow-repeat me-2"></i>Wagering</th>
              <th><i className="bi bi-wallet2 me-2"></i>Min Deposit</th>
              <th><i className="bi bi-link-45deg me-2"></i>Source</th>
            </tr>
          </thead>

          <tbody>
            {bonuses.map((bonus) => (
              <tr key={bonus.casino}>
                <td className="fw-semibold">{bonus.casino}</td>
                <td>{bonus.welcomeBonus}</td>
                <td>
                  <span className="badge text-bg-light border">
                    {bonus.wageringRequirement}x
                  </span>
                </td>
                <td>{bonus.minimumDeposit}</td>
                <td>
                  <SourceLink url={bonus.sourceUrl} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  )
}

export default BonusTable
