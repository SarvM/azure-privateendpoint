import React, { useEffect, useState } from "react";
import axios from "axios";

const ApiRequestComponent: React.FC = () => {
  const [responseData, setResponseData] = useState<object | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(
          "https://funapp-test-pep.azurewebsites.net/api/fetch-aztables?code=jEEeq6jGH_BEydPaaGpP_Z4CC6y7QQkZRFjr5K5S7HQ-AzFuUmL7aA%3D%3D",
          {
            headers: {},
          }
        );
        setResponseData(response.data);
        setLoading(false);
      } catch (error) {
        console.error("API call failed:", error);
        setError("Failed to fetch data");
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h1>API Response</h1>
      <pre>{JSON.stringify(responseData, null, 2)}</pre>
    </div>
  );
};

export default ApiRequestComponent;
