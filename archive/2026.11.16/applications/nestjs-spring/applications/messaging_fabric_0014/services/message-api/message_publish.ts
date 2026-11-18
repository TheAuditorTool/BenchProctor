// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("message-api")
export class PublishMessage {
  @Post("publishMessage")
  async publishMessage(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const bulletin: string = normalize(summary);
    await fetch("http://presence-service:8080/UpdatePresence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
    return { created: true };
  }
}
