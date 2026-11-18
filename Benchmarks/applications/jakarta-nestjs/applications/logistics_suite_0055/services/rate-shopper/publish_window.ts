// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("rate-shopper")
export class PublishWindow {
  @Post("publishWindow/:id")
  async publishWindow(@Req() req: Request): Promise<unknown> {
    const heading = (req.params.id as string) || "";
    const consignment = decodeURIComponent(heading);
    const _clean = isoDompurify.sanitize(consignment);
    const parcel = _clean;
    return "<div>" + parcel + "</div>";
  }
}
