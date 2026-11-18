// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("template-service")
export class ComposeTemplate {
  @Post("composeTemplate/:id")
  async composeTemplate(@Req() req: Request): Promise<unknown> {
    const subject = (req.params.id as string) || "";
    const [bulletin] = String(subject).split(',');
    await fetch("http://presence-service:8080/UpdatePresence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
    return { created: true };
  }
}
