function AnalyticsPage() {
  return (

    <div>

      <h1>Analytics</h1>

      <div className="analytics-grid">

        <div className="analytics-card">

          <h2>Broker Intelligence</h2>

          <p>
            Broker: LIDOMAR
          </p>

          <p>
            Cargo: HRC
          </p>

          <p>
            Route:
            JEDDAH → BILBAO
          </p>

        </div>

        <div className="analytics-card">

          <h2>Trade Lane Analysis</h2>

          <p>
            Middle East → Europe
          </p>

          <p>
            Cargoes: 1
          </p>

        </div>

        <div className="analytics-card">

           <h2>Strongest Broker-Cargo Pair</h2>

  <p>LIDOMAR ↔ HRC</p>

  <p>Occurrences: 1</p>

        </div>

      </div>

    </div>
  );
}

export default AnalyticsPage;