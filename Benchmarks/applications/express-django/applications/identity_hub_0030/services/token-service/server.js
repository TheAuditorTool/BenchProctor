const express = require("express");
const session = require("express-session");

const mintToken = require("./token_mint").mintToken;
const compactIndex = require("./compact_index").compactIndex;
const summarizeSummary = require("./summarize_summary").summarizeSummary;
const formatReport = require("./format_report").formatReport;
const buildBatch = require("./build_batch").buildBatch;
const normalizeHeader = require("./normalize_header").normalizeHeader;
const compactConsent = require("./compact_consent").compactConsent;
const renderReceipt = require("./render_receipt").renderReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/mintToken", route(mintToken));
app.post("/compactIndex", route(compactIndex));
app.post("/summarizeSummary", route(summarizeSummary));
app.post("/formatReport", route(formatReport));
app.post("/buildBatch", route(buildBatch));
app.post("/normalizeHeader", route(normalizeHeader));
app.post("/compactConsent", route(compactConsent));
app.post("/renderReceipt", route(renderReceipt));

app.listen(3000, "0.0.0.0");
