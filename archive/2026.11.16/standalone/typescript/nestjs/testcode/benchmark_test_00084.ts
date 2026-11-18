// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as net from "net";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

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
  @Post("BenchmarkTest00084")
  async BenchmarkTest00084(@Query("id") id: string): Promise<unknown> {
    const userInput = id || "";
    const data = decodeURIComponent(userInput);
    let _host = "";
    try { _host = new URL(String(data)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const targetUrl = data;
    net.connect(80, new URL(String(targetUrl)).hostname);
    return { created: true };
  }
}
