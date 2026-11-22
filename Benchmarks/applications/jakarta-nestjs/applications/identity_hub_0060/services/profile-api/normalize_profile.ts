// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("profile-api")
export class NormalizeProfile {
  @Post("normalizeProfile/:id")
  async normalizeProfile(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.params.id as string) || "";
    const _raw = paragraph;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(persona);
    const blurb = _clean;
    return "<div>" + blurb + "</div>";
  }
}
