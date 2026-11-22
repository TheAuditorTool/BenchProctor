const express = require("express");
const session = require("express-session");

const queueFulfillment = require("./fulfillment_queue").queueFulfillment;
const normalizePromotion = require("./normalize_promotion").normalizePromotion;
const compactSummary = require("./compact_summary").compactSummary;
const verifyPolicy = require("./verify_policy").verifyPolicy;
const formatCart = require("./format_cart").formatCart;
const compactConfig = require("./compact_config").compactConfig;
const exportReport = require("./export_report").exportReport;
const validateManifest = require("./validate_manifest").validateManifest;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/queueFulfillment", route(queueFulfillment));
app.post("/normalizePromotion", route(normalizePromotion));
app.post("/compactSummary", route(compactSummary));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/formatCart", route(formatCart));
app.post("/compactConfig", route(compactConfig));
app.post("/exportReport", route(exportReport));
app.post("/validateManifest", route(validateManifest));

app.listen(3000, "0.0.0.0");
