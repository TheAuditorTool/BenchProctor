// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("message-api")
export class PublishMessage {
  @Post("publishMessage")
  async publishMessage(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.origin as string) || "";
    const _input = String(summary);
    let bulletin;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': bulletin = _input.normalize('NFC'); break;
      default: bulletin = _input; break;
    }
    await fetch("http://bounce-handler:8080/RecordBounce", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({messaging_payload: bulletin})});
    return { created: true };
  }
}
