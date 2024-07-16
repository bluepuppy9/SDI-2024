import {defineStore} from 'pinia'
import { supabase } from '@/lib/supabaseClient'

import { ref } from 'vue'

export const useStore = defineStore('store', () => {

    const classes = ref()

    const getClasses = async () => {
        const { data, error } = await supabase
          .from('profiles')
          .select('username')
          .eq('id', '4697e949-d4ce-4e0b-89fc-34b3772ec4f6')
        if (error) {
          console.log(error)
        } else {
          classes.value = data
        }
      }
    getClasses()
    return { classes, getClasses }
}
)