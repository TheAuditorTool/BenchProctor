import express, { Request, Response } from "express";
import session from "express-session";

import { dispatchCarrier } from "./carrier_dispatch";
import { renderRoster } from "./render_roster";
import { formatReceipt } from "./format_receipt";
import { rotateWaybill } from "./rotate_waybill";
import { pruneSummary } from "./prune_summary";
import { publishPolicy } from "./publish_policy";
import { verifyBundle } from "./verify_bundle";
import { validateSummary } from "./validate_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", dispatchCarrier);
app.post("/renderRoster", renderRoster);
app.post("/formatReceipt", formatReceipt);
app.post("/rotateWaybill", rotateWaybill);
app.post("/pruneSummary", pruneSummary);
app.post("/publishPolicy", publishPolicy);
app.post("/verifyBundle/:id", verifyBundle);
app.post("/validateSummary/:id", validateSummary);

app.listen(3000, "0.0.0.0");
