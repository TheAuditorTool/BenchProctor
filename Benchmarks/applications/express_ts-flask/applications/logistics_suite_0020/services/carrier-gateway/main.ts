import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

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
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", route(dispatchCarrier));
app.post("/renderRoster", route(renderRoster));
app.post("/formatReceipt", route(formatReceipt));
app.post("/rotateWaybill", route(rotateWaybill));
app.post("/pruneSummary", route(pruneSummary));
app.post("/publishPolicy", route(publishPolicy));
app.post("/verifyBundle", route(verifyBundle));
app.post("/validateSummary", route(validateSummary));

app.listen(3000, "0.0.0.0");
