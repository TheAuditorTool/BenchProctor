// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("address-validator")
export class AnnotateWindow {
  @Post("annotateWindow")
  async annotateWindow(@Req() req: Request): Promise<unknown> {
    const summary = (req.body.field as string) || "";
    const consignment = decodeURIComponent(summary);
    const _clean = isoDompurify.sanitize(consignment);
    const parcel = _clean;
    return "<div>" + parcel + "</div>";
  }
}
