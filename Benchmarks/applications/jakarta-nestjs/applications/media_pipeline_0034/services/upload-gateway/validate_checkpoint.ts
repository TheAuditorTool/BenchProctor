// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("upload-gateway")
export class ValidateCheckpoint {
  @Post("validateCheckpoint/:id")
  async validateCheckpoint(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.params.id as string) || "";
    const _raw = synopsis;
    const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
    const _clean = isoDompurify.sanitize(rendition);
    const montage = _clean;
    return "<div>" + montage + "</div>";
  }
}
