import { useState, useEffect } from 'react';
import {
  Box,
  Container,
  TextField,
  Button,
  Typography,
  Paper,
  CircularProgress,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  ThemeProvider,
  createTheme,
  CssBaseline,
} from '@mui/material';
import { motion } from 'framer-motion';
import axios from 'axios';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#6C63FF',
    },
    secondary: {
      main: '#FF6584',
    },
    background: {
      default: '#1A1A1A',
      paper: '#2D2D2D',
    },
  },
  typography: {
    fontFamily: '"Poppins", "Roboto", "Helvetica", "Arial", sans-serif',
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 8,
          textTransform: 'none',
          padding: '12px 24px',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 16,
        },
      },
    },
  },
});

// Hardcode the URL since env variable isn't working
const API_URL = 'https://ai-map-generator-6ea864cf7c85.herokuapp.com';
console.log('API URL:', API_URL);

function App() {
  console.log('App component rendering...');

  useEffect(() => {
    console.log('App component mounted');
  }, []);

  const [prompt, setPrompt] = useState('');
  const [style, setStyle] = useState('realistic');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [mapUrl, setMapUrl] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setMapUrl('');

    try {
      console.log('Sending request to backend...');
      const response = await axios.post(`${API_URL}/generate-map`, {
        prompt,
        style,
      });
      console.log('Received response:', response.data);
      setMapUrl(response.data.url);
    } catch (err: any) {
      console.error('Error details:', err.response?.data || err.message);
      setError(err.response?.data?.detail || 'Failed to generate map. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Container maxWidth="lg">
        <Box
          sx={{
            minHeight: '100vh',
            py: 4,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            gap: 4,
            color: 'white',
          }}
        >
          <motion.div
            initial={{ y: -20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.5 }}
          >
            <Typography
              variant="h2"
              component="h1"
              sx={{
                fontWeight: 700,
                background: 'linear-gradient(45deg, #6C63FF 30%, #FF6584 90%)',
                WebkitBackgroundClip: 'text',
                WebkitTextFillColor: 'transparent',
                mb: 2,
                color: 'white',
              }}
            >
              AI Map Generator
            </Typography>
          </motion.div>

          <Paper
            component={motion.div}
            initial={{ scale: 0.95, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.5 }}
            elevation={3}
            sx={{ 
              p: 4, 
              width: '100%', 
              maxWidth: 600,
              backgroundColor: '#2D2D2D',
            }}
          >
            <form onSubmit={handleSubmit}>
              <TextField
                fullWidth
                label="Describe the map you want to generate"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                multiline
                rows={3}
                sx={{ 
                  mb: 3,
                  '& .MuiInputBase-input': {
                    color: 'white',
                  },
                  '& .MuiInputLabel-root': {
                    color: 'white',
                  },
                }}
              />

              <FormControl 
                fullWidth 
                sx={{ 
                  mb: 3,
                  '& .MuiInputBase-input': {
                    color: 'white',
                  },
                  '& .MuiInputLabel-root': {
                    color: 'white',
                  },
                }}
              >
                <InputLabel>Map Style</InputLabel>
                <Select
                  value={style}
                  label="Map Style"
                  onChange={(e) => setStyle(e.target.value)}
                >
                  <MenuItem value="realistic">Realistic</MenuItem>
                  <MenuItem value="fantasy">Fantasy</MenuItem>
                  <MenuItem value="vintage">Vintage</MenuItem>
                  <MenuItem value="minimalist">Minimalist</MenuItem>
                </Select>
              </FormControl>

              <Button
                type="submit"
                variant="contained"
                fullWidth
                size="large"
                disabled={loading || !prompt}
                sx={{
                  background: 'linear-gradient(45deg, #6C63FF 30%, #FF6584 90%)',
                  color: 'white',
                }}
              >
                {loading ? <CircularProgress size={24} /> : 'Generate Map'}
              </Button>
            </form>
          </Paper>

          {error && (
            <Typography color="error" sx={{ mt: 2 }}>
              {error}
            </Typography>
          )}

          {mapUrl && (
            <Paper
              component={motion.div}
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{ duration: 0.5 }}
              elevation={3}
              sx={{ p: 2, width: '100%', maxWidth: 800 }}
            >
              <img
                src={mapUrl}
                alt="Generated map"
                style={{
                  width: '100%',
                  height: 'auto',
                  borderRadius: 8,
                }}
              />
            </Paper>
          )}
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App; 
