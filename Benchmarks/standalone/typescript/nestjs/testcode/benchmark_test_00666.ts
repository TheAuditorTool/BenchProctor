// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Header, Post, UsePipes, ValidationPipe } from "@nestjs/common";
import { Response } from "express";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00666")
  @UsePipes(new ValidationPipe())
  @Header("Content-Type", "text/html")
  async BenchmarkTest00666(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    const [data] = String(userInput).split(',');
    return "<div>" + data + "</div>";
  }
}
