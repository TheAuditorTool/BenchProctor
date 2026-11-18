// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("delivery-service")
export class DispatchDelivery {
  @Post("dispatchDelivery")
  async dispatchDelivery(@Req() req: Request): Promise<unknown> {
    const preface = req.body.messaging_payload || "";
    return "<div>" + preface + "</div>";
  }
}
