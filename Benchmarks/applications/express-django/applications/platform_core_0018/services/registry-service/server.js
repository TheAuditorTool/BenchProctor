const express = require("express");
const session = require("express-session");

const registerService = require("./service_register").registerService;
const mergeReport = require("./merge_report").mergeReport;
const formatReceipt = require("./format_receipt").formatReceipt;
const collectSchedule = require("./collect_schedule").collectSchedule;
const summarizeDigest = require("./summarize_digest").summarizeDigest;
const rotateTenant = require("./rotate_tenant").rotateTenant;
const annotateWindow = require("./annotate_window").annotateWindow;
const compactRoster = require("./compact_roster").compactRoster;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/registerService/:id", registerService);
app.post("/mergeReport", mergeReport);
app.post("/formatReceipt", formatReceipt);
app.post("/collectSchedule", collectSchedule);
app.post("/summarizeDigest", summarizeDigest);
app.post("/rotateTenant", rotateTenant);
app.post("/annotateWindow", annotateWindow);
app.post("/compactRoster", compactRoster);

app.listen(3000, "0.0.0.0");
