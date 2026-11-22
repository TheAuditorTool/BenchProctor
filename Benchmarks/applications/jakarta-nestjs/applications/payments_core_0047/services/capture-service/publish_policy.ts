// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("capture-service")
export class PublishPolicy {
  @Post("publishPolicy/:id")
  async publishPolicy(@Req() req: Request): Promise<unknown> {
    const footnote = (req.params.id as string) || "";
    const _raw = footnote;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(remittance);
    const disbursement = _clean;
    return "<div>" + disbursement + "</div>";
  }
}
