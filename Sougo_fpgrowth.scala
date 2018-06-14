import scopt.OptionParser

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.mllib.fpm.FPGrowth
import org.apache.spark.mllib.fpm.FPGrowthModel
import org.apache.spark.rdd.RDD

Object FPGrowth {

	def main(args: Array[String]) {
		val conf = new SparkConf().setAppName(s"FPGrowthExample")
    	val sc = new SparkContext(conf)
    	val transactions = sc.textFile("hdfs://10.141.208.44:9000/user/hadoop/smy/SougoJ2.txt").map(s => s.trim.split(" ")).cache()

    	println(s"Number of transactions: ${transactions.count()}")

    	val model = new FPGrowth().setMinSupport(0.00001).setNumPartitions(10)

      	val fmodel = model.run(transactions)

    	println(s"Number of frequent itemsets: ${model.freqItemsets.count()}")

    	fmodel.freqItemsets.collect().foreach { itemset =>
      		println(s"${itemset.items.mkString("[", ",", "]")}, ${itemset.freq}")
    	}

    	fmodel.freqItemsets.saveAsTextFile("hdfs://")

    	sc.stop()
	}

}