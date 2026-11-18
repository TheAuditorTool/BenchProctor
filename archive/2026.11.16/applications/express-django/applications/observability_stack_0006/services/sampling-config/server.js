const express = require("express");
const session = require("express-session");

const configureSample = require("./sample_config").configureSample;
const collectSnapshot = require("./collect_snapshot").collectSnapshot;
const resolveSummary = require("./resolve_summary").resolveSummary;
const fetchWindow = require("./fetch_window").fetchWindow;
const fetchConfig = require("./fetch_config").fetchConfig;
const compactPolicy = require("./compact_policy").compactPolicy;
const summarizeSnapshot = require("./summarize_snapshot").summarizeSnapshot;
const archiveSummary = require("./archive_summary").archiveSummary;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/configureSample", route(configureSample));
app.post("/collectSnapshot", route(collectSnapshot));
app.post("/resolveSummary", route(resolveSummary));
app.post("/fetchWindow", route(fetchWindow));
app.post("/fetchConfig", route(fetchConfig));
app.post("/compactPolicy", route(compactPolicy));
app.post("/summarizeSnapshot", route(summarizeSnapshot));
app.post("/archiveSummary", route(archiveSummary));

app.listen(3000, "0.0.0.0");
