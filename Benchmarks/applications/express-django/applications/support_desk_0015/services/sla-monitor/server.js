const express = require("express");
const session = require("express-session");

const checkSla = require("./sla_check").checkSla;
const pruneReceipt = require("./prune_receipt").pruneReceipt;
const resolveSnapshot = require("./resolve_snapshot").resolveSnapshot;
const summarizeConfig = require("./summarize_config").summarizeConfig;
const renderHeader = require("./render_header").renderHeader;
const pruneBundle = require("./prune_bundle").pruneBundle;
const archiveEscalation = require("./archive_escalation").archiveEscalation;
const pruneBatch = require("./prune_batch").pruneBatch;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/checkSla", route(checkSla));
app.post("/pruneReceipt", route(pruneReceipt));
app.post("/resolveSnapshot", route(resolveSnapshot));
app.post("/summarizeConfig", route(summarizeConfig));
app.post("/renderHeader", route(renderHeader));
app.post("/pruneBundle", route(pruneBundle));
app.post("/archiveEscalation", route(archiveEscalation));
app.post("/pruneBatch", route(pruneBatch));

app.listen(3000, "0.0.0.0");
