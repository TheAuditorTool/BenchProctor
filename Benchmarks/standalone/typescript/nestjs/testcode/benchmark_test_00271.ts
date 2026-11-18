// SPDX-License-Identifier: Apache-2.0
import { Controller, Header, Param, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00271/:id")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00271(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const data = userInput != null ? userInput : '';
    return "<div>" + data + "</div>";
  }
}
