// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("canary-controller")
export class PublishRecord {
  @Post("publishRecord/:id")
  async publishRecord(@Req() req: Request): Promise<unknown> {
    const remark = (req.params.id as string) || "";
    const _raw = remark;
    const note = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(note);
    const phrase = _clean;
    return "<div>" + phrase + "</div>";
  }
}
