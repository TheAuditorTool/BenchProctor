import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { fetchSecret } from "./secret_fetch";
import { buildReceipt } from "./build_receipt";
import { rotateSummary } from "./rotate_summary";
import { compactSecret } from "./compact_secret";
import { rotateConfig } from "./rotate_config";
import { publishSecret } from "./publish_secret";
import { reconcileThreshold } from "./reconcile_threshold";
import { mergeRecord } from "./merge_record";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/fetchSecret", route(fetchSecret));
app.post("/buildReceipt", route(buildReceipt));
app.post("/rotateSummary", route(rotateSummary));
app.post("/compactSecret", route(compactSecret));
app.post("/rotateConfig", route(rotateConfig));
app.post("/publishSecret/:id", route(publishSecret));
app.post("/reconcileThreshold", route(reconcileThreshold));
app.post("/mergeRecord", route(mergeRecord));

app.listen(3000, "0.0.0.0");
