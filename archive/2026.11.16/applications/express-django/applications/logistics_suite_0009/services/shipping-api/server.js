const express = require("express");
const session = require("express-session");

const quoteShipment = require("./shipment_quote").quoteShipment;
const resolveLedger = require("./resolve_ledger").resolveLedger;
const buildRoster = require("./build_roster").buildRoster;
const renderCheckpoint = require("./render_checkpoint").renderCheckpoint;
const mergeWindow = require("./merge_window").mergeWindow;
const formatReceipt = require("./format_receipt").formatReceipt;
const compactCarrier = require("./compact_carrier").compactCarrier;
const annotateSnapshot = require("./annotate_snapshot").annotateSnapshot;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/quoteShipment", route(quoteShipment));
app.post("/resolveLedger", route(resolveLedger));
app.post("/buildRoster", route(buildRoster));
app.post("/renderCheckpoint", route(renderCheckpoint));
app.post("/mergeWindow", route(mergeWindow));
app.post("/formatReceipt", route(formatReceipt));
app.post("/compactCarrier", route(compactCarrier));
app.post("/annotateSnapshot", route(annotateSnapshot));

app.listen(3000, "0.0.0.0");
