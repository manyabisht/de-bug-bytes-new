import 'bootstrap/dist/css/bootstrap.min.css';

import React, { useState, useEffect } from 'react';
import { Button, Card, Tab, Tabs, Alert, Spinner } from 'react-bootstrap';  // Importing from React Bootstrap

// Mock data - replace with actual API calls
const mockData = [
  {
    id: 1,
    title: "Thailand Adventure",
    description: "Explore the beautiful beaches and temples of Thailand",
    duration_days: 7,
    base_price: 1299.99,
    destination: "Thailand",
    totalUsers: 2854
  },
  {
    id: 2,
    title: "Japan Cultural Tour",
    description: "Experience the rich culture and history of Japan",
    duration_days: 10,
    base_price: 2499.99,
    destination: "Japan",
    totalUsers: 2960
  }
];

const App = () => {
  const [packages, setPackages] = useState(mockData);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState('packages');

  const fetchPackages = async () => {
    setLoading(true);
    try {
      await new Promise(resolve => setTimeout(resolve, 1000));
      setPackages(mockData);
      setError(null);
    } catch (err) {
      setError('Failed to fetch packages. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPackages();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 p-4">
      <div className="max-w-7xl mx-auto">
        <header className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">TBO Travel Agent Portal</h1>
          <p className="text-gray-600 mt-2">Manage your travel packages and bookings</p>
        </header>

        <Tabs defaultActiveKey={activeTab} onSelect={setActiveTab} id="travel-tabs" className="mb-3">
          <Tab eventKey="packages" title="Packages">
            {error && <Alert variant="danger">{error}</Alert>}

            {loading ? (
              <div className="d-flex justify-content-center align-items-center p-5">
                <Spinner animation="border" />
              </div>
            ) : (
              <div className="d-flex flex-wrap justify-content-between">
                {packages.map((pkg) => (
                  <Card key={pkg.id} style={{ width: '18rem' }} className="mb-4">
                    <Card.Body>
                      <Card.Title>{pkg.title}</Card.Title>
                      <Card.Subtitle className="mb-2 text-muted">{pkg.duration_days} days</Card.Subtitle>
                      <Card.Text>{pkg.description}</Card.Text>
                      <div className="d-flex justify-content-between align-items-center">
                        <p className="font-weight-bold">${pkg.base_price}</p>
                        <Button variant="outline-primary" size="sm">View Details</Button>
                      </div>
                      <div className="d-flex justify-content-between text-muted mt-2">
                        <span>Destination: {pkg.destination}</span>
                        <span>{pkg.totalUsers} bookings</span>
                      </div>
                    </Card.Body>
                  </Card>
                ))}
              </div>
            )}
          </Tab>

          <Tab eventKey="bookings" title="Bookings">
            <Card>
              <Card.Body>
                <p>Bookings management coming soon...</p>
              </Card.Body>
            </Card>
          </Tab>

          <Tab eventKey="customers" title="Customers">
            <Card>
              <Card.Body>
                <p>Customer management coming soon...</p>
              </Card.Body>
            </Card>
          </Tab>
        </Tabs>
      </div>
    </div>
  );
};

export default App;
