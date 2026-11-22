// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import isoDompurify from "isomorphic-dompurify";

@Controller("delivery-service")
export class DispatchDelivery {
  @Post("dispatchDelivery")
  async dispatchDelivery(@Req() req: Request): Promise<unknown> {
    const remark = req.body.messaging_payload || "";
    const _clean = isoDompurify.sanitize(remark);
    const citation = _clean;
    return "<div>" + citation + "</div>";
  }
}
