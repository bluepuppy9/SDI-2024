import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://uanyfbgwnzvjywjmbrro.supabase.co'
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVhbnlmYmd3bnp2anl3am1icnJvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjExMzQxMDEsImV4cCI6MjAzNjcxMDEwMX0.2pvmNRp_YvZ096st3OWnvpZSlGig-Jm0MddFPtZGPHs'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)