// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("partner-registry")
export class VerifyConnector {
  @Post("verifyConnector")
  async verifyConnector(@Req() req: Request): Promise<unknown> {
    const citation = (req.body?.field as string) || "";
    const handshake = decodeURIComponent(citation);
    const _clean = isoDompurify.sanitize(handshake);
    const heading = _clean;
    return "<div>" + heading + "</div>";
  }
}
