import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { publishMessage } from "./message_publish";
import { annotateManifest } from "./annotate_manifest";
import { normalizeSnapshot } from "./normalize_snapshot";
import { formatBatch } from "./format_batch";
import { verifyWindow } from "./verify_window";
import { annotateDelivery } from "./annotate_delivery";
import { resolveDigest } from "./resolve_digest";
import { validateSnapshot } from "./validate_snapshot";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/publishMessage", route(publishMessage));
app.post("/annotateManifest", route(annotateManifest));
app.post("/normalizeSnapshot", route(normalizeSnapshot));
app.post("/formatBatch", route(formatBatch));
app.post("/verifyWindow", route(verifyWindow));
app.post("/annotateDelivery", route(annotateDelivery));
app.post("/resolveDigest", route(resolveDigest));
app.post("/validateSnapshot", route(validateSnapshot));

app.listen(3000, "0.0.0.0");
