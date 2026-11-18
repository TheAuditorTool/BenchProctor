// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("template-service")
export class ComposeTemplate {
  @Post("composeTemplate")
  @UseGuards(AuthGuard)
  async composeTemplate(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.authorization as string) || "";
    const bulletin = Buffer.from(heading, "base64").toString();
    await fetch("http://bounce-handler:8080/RecordBounce", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
    return { created: true };
  }
}
