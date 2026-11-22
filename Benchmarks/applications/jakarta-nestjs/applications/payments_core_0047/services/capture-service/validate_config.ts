// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("capture-service")
export class ValidateConfig {
  @Post("validateConfig")
  async validateConfig(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.field as string) || "";
    const remittance = decodeURIComponent(footnote);
    const _clean = isoDompurify.sanitize(remittance);
    const disbursement = _clean;
    return "<div>" + disbursement + "</div>";
  }
}
