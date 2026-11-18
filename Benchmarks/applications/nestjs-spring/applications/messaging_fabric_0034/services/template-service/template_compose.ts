// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("template-service")
export class ComposeTemplate {
  @Post("composeTemplate")
  async composeTemplate(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.authorization as string) || "";
    const tokens = String(footnote).split(',').filter((t) => t.length > 0);
    const bulletin = tokens.join(' ');
    await fetch("http://delivery-service:8080/DispatchDelivery", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
    return { created: true };
  }
}
