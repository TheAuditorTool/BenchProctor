const express = require("express");
const session = require("express-session");

const convertFx = require("./fx_convert").convertFx;
const compactDigest = require("./compact_digest").compactDigest;
const normalizeLedger = require("./normalize_ledger").normalizeLedger;
const summarizeWallet = require("./summarize_wallet").summarizeWallet;
const renderWindow = require("./render_window").renderWindow;
const resolveWallet = require("./resolve_wallet").resolveWallet;
const mergeBundle = require("./merge_bundle").mergeBundle;
const archiveReport = require("./archive_report").archiveReport;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/convertFx", route(convertFx));
app.post("/compactDigest", route(compactDigest));
app.post("/normalizeLedger", route(normalizeLedger));
app.post("/summarizeWallet", route(summarizeWallet));
app.post("/renderWindow", route(renderWindow));
app.post("/resolveWallet", route(resolveWallet));
app.post("/mergeBundle/:id", route(mergeBundle));
app.post("/archiveReport", route(archiveReport));

app.listen(3000, "0.0.0.0");
