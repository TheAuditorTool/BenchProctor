// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("refund-service")
export class IssueRefund {
  @Post("issueRefund")
  async issueRefund(@Req() req: Request): Promise<unknown> {
    const arrears = req.body.billing_payload || "";
    http.get(arrears);
    return { created: true };
  }
}
