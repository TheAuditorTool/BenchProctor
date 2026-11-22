const express = require("express");
const session = require("express-session");
const multer = require("multer");

const placeOrder = require("./order_submit").placeOrder;
const formatBatch = require("./format_batch").formatBatch;
const normalizePromotion = require("./normalize_promotion").normalizePromotion;
const formatReport = require("./format_report").formatReport;
const validateFulfillment = require("./validate_fulfillment").validateFulfillment;
const publishPolicy = require("./publish_policy").publishPolicy;
const pruneConfig = require("./prune_config").pruneConfig;
const summarizeCheckpoint = require("./summarize_checkpoint").summarizeCheckpoint;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/placeOrder", route(placeOrder));
app.post("/formatBatch", route(formatBatch));
app.post("/normalizePromotion", route(normalizePromotion));
app.post("/formatReport", route(formatReport));
app.post("/validateFulfillment", route(validateFulfillment));
app.post("/publishPolicy", route(publishPolicy));
app.post("/pruneConfig", route(pruneConfig));
app.post("/summarizeCheckpoint", route(summarizeCheckpoint));

app.listen(3000, "0.0.0.0");
