// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as http from "http";
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
  @Post("BenchmarkTest00360")
  async BenchmarkTest00360(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    const data = `${userInput}`;
    let _host = "";
    try { _host = new URL(String(data)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const targetUrl = data;
    http.get(targetUrl);
    return { created: true };
  }
}
