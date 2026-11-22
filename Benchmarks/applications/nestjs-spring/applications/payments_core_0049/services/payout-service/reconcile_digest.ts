// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("payout-service")
export class ReconcileDigest {
  @Post("reconcileDigest")
  async reconcileDigest(@Req() req: Request): Promise<unknown> {
    const headline = (req.cookies?.session_token as string) || "";
    const transform = (v: string): string => v.trim();
    const disbursement: string = transform(headline);
    const _clean = isoDompurify.sanitize(disbursement);
    const remittance = _clean;
    return new StreamableFile(Buffer.from("<section>" + remittance + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
