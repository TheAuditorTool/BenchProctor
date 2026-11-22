// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("quota-service")
export class ValidateQuota {
  @Post("validateQuota/:id")
  async validateQuota(@Req() req: Request): Promise<unknown> {
    const heading = (req.params.id as string) || "";
    const _raw = heading;
    const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(handshake);
    const persona = _clean;
    return "<div>" + persona + "</div>";
  }
}
