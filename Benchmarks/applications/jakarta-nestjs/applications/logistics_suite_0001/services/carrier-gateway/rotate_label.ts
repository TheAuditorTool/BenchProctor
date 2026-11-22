// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("carrier-gateway")
export class RotateLabel {
  @Post("rotateLabel")
  async rotateLabel(@Req() req: Request): Promise<unknown> {
    const quotation = (req.body.field as string) || "";
    const parcel = decodeURIComponent(quotation);
    const _clean = isoDompurify.sanitize(parcel);
    const consignment = _clean;
    return "<div>" + consignment + "</div>";
  }
}
