import bonuses from '../data/bonuses.json'
import SourceLink from './SourceLink'

function BonusTable() {
  return (
    <section className="fade-in">
      <div className="mb-4">
        <h2 className="h4 fw-bold mb-1">Current bonus offers</h2>
        <p className="text-secondary mb-0">
          Three offers collected from a public casino comparison source.
        </p>
      </div>

      <div className="table-responsive">
        <table className="table align-middle mb-0">
          <thead>
            <tr>
              <th>Casino</th>
              <th>Welcome Bonus</th>
              <th>Wagering</th>
              <th>Minimum Deposit</th>
              <th>Source</th>
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
