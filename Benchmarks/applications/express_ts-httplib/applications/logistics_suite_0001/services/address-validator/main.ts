import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { validateAddress } from "./address_validate";
import { summarizeShipment } from "./summarize_shipment";
import { enrichIndex } from "./enrich_index";
import { validateDigest } from "./validate_digest";
import { exportSummary } from "./export_summary";
import { fetchDigest } from "./fetch_digest";
import { exportReceipt } from "./export_receipt";
import { pruneCheckpoint } from "./prune_checkpoint";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/validateAddress", route(validateAddress));
app.post("/summarizeShipment", route(summarizeShipment));
app.post("/enrichIndex", route(enrichIndex));
app.post("/validateDigest", route(validateDigest));
app.post("/exportSummary", route(exportSummary));
app.post("/fetchDigest", route(fetchDigest));
app.post("/exportReceipt", route(exportReceipt));
app.post("/pruneCheckpoint", route(pruneCheckpoint));

app.listen(3000, "0.0.0.0");
