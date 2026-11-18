// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as net from "net";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { createClient } from "redis";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00673")
  async BenchmarkTest00673(): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const userInput = (await _cache.get("user_data")) || "";
    const data = Buffer.from(userInput, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(data)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const targetUrl = data;
    net.connect(80, new URL(String(targetUrl)).hostname);
    return { created: true };
  }
}
