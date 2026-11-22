import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { queueFulfillment } from "./fulfillment_queue";
import { normalizePromotion } from "./normalize_promotion";
import { compactSummary } from "./compact_summary";
import { verifyPolicy } from "./verify_policy";
import { formatCart } from "./format_cart";
import { compactConfig } from "./compact_config";
import { exportReport } from "./export_report";
import { validateManifest } from "./validate_manifest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/queueFulfillment", route(queueFulfillment));
app.post("/normalizePromotion", route(normalizePromotion));
app.post("/compactSummary", route(compactSummary));
app.post("/verifyPolicy", route(verifyPolicy));
app.post("/formatCart/:id", route(formatCart));
app.post("/compactConfig", route(compactConfig));
app.post("/exportReport", route(exportReport));
app.post("/validateManifest", route(validateManifest));

app.listen(3000, "0.0.0.0");
